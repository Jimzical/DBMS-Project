 DELIMITER //

    CREATE PROCEDURE DisplayTableRecords(IN tableName VARCHAR(255))
    BEGIN
        IF EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = tableName) THEN
            SET @query = CONCAT('SELECT * FROM ', tableName);
            PREPARE stmt FROM @query;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;
        ELSE
            SELECT 'Table does not exist.' AS Message;
        END IF;
    END //

DELIMITER ;