-- list things

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states Where name = "California") ORDER BY id ASC;