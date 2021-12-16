CREATE_SONGS_TABLE = f"""
        CREATE TABLE IF NOT EXISTS `songs` (
            `song_id` MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT
        ,   `song_name` VARCHAR(250) NOT NULL
        ,   `fingerprinted` TINYINT DEFAULT 0
        ,   `file_sha1` BINARY(20) NOT NULL
        ,   `total_hashes` INT NOT NULL DEFAULT 0
        ,   `date_created` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ,   `date_modified` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        ,   CONSTRAINT `pk_songs_song_id` PRIMARY KEY (`song_id`)
        ,   CONSTRAINT `uq_songs_song_id` UNIQUE KEY (`song_id`)
        ) ENGINE=INNODB;
    """