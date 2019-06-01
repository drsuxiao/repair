use repair;
SET SQL_SAFE_UPDATES = 0;
insert into department(id,code,name) values
(1,'001','(厢竹)产科MICU'),
(2,'002','(厢竹)产一科'),
(3,'003','(厢竹)新生儿科重症组');

insert into equipment_brand(id,code,name) values
(1,'001','联想'),
(2,'002','惠普'),
(3,'003','其他品牌');

insert into equipment_type(id,code,name) values
(1,'001','主机'),
(2,'002','一体机'),
(3,'003','显示器');

insert into equipment_fault(id,code,name) values
(1,'001','主板故障'),
(2,'002','电源烧了'),
(3,'003','显示屏坏了');

insert into repair_company(id,code,name) values
(1,'001','联想'),
(2,'002','惠普'),
(3,'003','其他品牌');
insert into equipment_repair
(id,repair_date,dept_code,brand_code,type_code,equipment_code,fault_code,com_code) 
values(5,'2019-05-20','001','001','001','sa98765467','001','001'),
(6,'2019-05-26','003','002','002','sa9999999','002','002'),
(7,'2019-05-25','001','003','002','sa8844776','001','003'),
(8,'2019-05-25','003','003','002','sa8128796','002','003');