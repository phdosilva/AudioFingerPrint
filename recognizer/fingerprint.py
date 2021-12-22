import hashlib
import sys

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import binary_erosion

np.set_printoptions(threshold=sys.maxsize)

# Default values:
DEFAULT_FS = 44100 # Number from search
WINDOW_SIZE = 4096
OVERLAP_SIZE = WINDOW_SIZE * 0.5
FAN_VALUE = 100

# Unknowing defaults
PEAK_NEIGHBORHOOD_SIZE = 20
DEFAULT_AMP_MIN = 10
MIN_HASH_TIME_DELTA = 0
MAX_HASH_TIME_DELTA = 200
FINGERPRINT_REDUCTION = 20


def print_plot(data, title):
    plt.plot(data)
    plt.title(title)
    plt.show()


def fingerprint(samples, wsize=WINDOW_SIZE, osize=OVERLAP_SIZE, Fs=DEFAULT_FS, fan_value=FAN_VALUE,
                amp_min=DEFAULT_AMP_MIN):
    spectrum_arr = mlab.specgram(
        x=samples,
        NFFT=wsize,
        Fs=Fs,
        window=mlab.window_hanning,
        noverlap=osize)[0]

    # debugger
    # print_plot(spectrum_arr[0], f'arr_2D')
    # print(len(spectrum_arr))

    # todo: Understand better this point
    spectrum_arr = 10 * np.log10(spectrum_arr)  # calculates the base 10 logarithm for all elements of arr_2D

    # debugger
    # print_plot(spectrum_arr, f'arr_2D about log')

    local_maxima = get_2D_peaks(spectrum_arr, amp_min)

    return generate_hashes(local_maxima, fan_value=fan_value)


def get_2D_peaks(arr2D, amp_min):
    # The initial idea is not consider the diagonals itens as neighborhood,
    # because they are further away. But not consider this itens is not relevant.

    # An array like this:
    #   T   T   T
    #   T   T   T
    #   T   T   T
    neighborhood = np.ones((PEAK_NEIGHBORHOOD_SIZE * 2 + 1, PEAK_NEIGHBORHOOD_SIZE * 2 + 1), dtype=bool)

    # Returns true to the picks
    local_max = maximum_filter(arr2D, footprint=neighborhood) == arr2D

    # todo: Testar se podemos desconsiderar este filtro
    # WHAT IS EROSION:
    # Erosion is a mathematical morphology operation that uses a structuring element for shrinking the shapes in an
    # image. The binary erosion of an image by a structuring element is the locus of the points where a
    # superimposition of the structuring element centered on the point is entirely contained in the set of non-zero
    # elements of the image.
    background = (arr2D == 0)
    eroded_background = binary_erosion(background, structure=neighborhood, border_value=1)
    detected_peaks = local_max != eroded_background
    # detected_peaks = local_max
    # in tests, without the eroded mask less matches are found

    amps = arr2D[detected_peaks]
    freqs, times = np.where(detected_peaks)

    amps = amps.flatten()

    filter_idxs = np.where(amps > amp_min)

    freqs_filter = freqs[filter_idxs]
    times_filter = times[filter_idxs]

    return list(zip(freqs_filter, times_filter))


def generate_hashes(peaks, fan_value):

    frequence_index = 0
    time_index = 1

    hashes = []
    for current_peak_index in range(len(peaks)):
        for neighbor_peak_index in range(current_peak_index+1,
                                         (current_peak_index + fan_value)
                                         if (current_peak_index + fan_value < len(peaks))
                                         else len(peaks)):

            freq_current_peak = peaks[current_peak_index][frequence_index]
            freq_neighbor_peak = peaks[neighbor_peak_index][frequence_index]

            absolute_time = peaks[current_peak_index][time_index]
            time_neighbor_peak = peaks[neighbor_peak_index][time_index]

            # t_delta is a relative time (relative to the other peak)
            t_delta = time_neighbor_peak - absolute_time

            # to not count values out from the estimate time between peaks
            if MIN_HASH_TIME_DELTA <= t_delta <= MAX_HASH_TIME_DELTA:
                h = hashlib.sha1(
                    f"{str(freq_current_peak)}|{str(freq_neighbor_peak)}|{str(t_delta)}".encode('utf-8'))

                hashes.append((h.hexdigest()[0:FINGERPRINT_REDUCTION], absolute_time))

    return hashes