SELECT * FROM repair.equipment_repair;

SET SQL_SAFE_UPDATES = 0;
update repair.equipment_repair set repair_status = 1;