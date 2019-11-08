select p.user_name, sum(p.price) as expenditures
from purchases as p
GROUP BY p.user_name

select sum(p.price) as expenditures_by_items
from purchases as p
GROUP BY p.item

SELECT  cast(count(u.name)as FLOAT)  / cast((select DISTINCT count(*) from users)as float) *100
from users as u
where u.name not in (select DISTINCT user_name from purchases)


SELECT cast(count(u.name) AS FLOAT)/CAST(3 as FLOAT)
from users as u
where u.name not in (select user_name from purchases)


SELECT extract(year from date_purchased) as year ,extract(month from date_purchased) as month, count(item) as No_of_items, item
from purchases
GROUP BY extract(year from date_purchased) ,extract(month from date_purchased), item


SELECT e.employee_name AS emp, e.employee_id, m.employee_name AS Manager, m.employee_id
FROM employees AS e LEFT OUTER JOIN employees AS m
ON e.manager_id =m.employee_id;



SELECT e.employee_name, td.training_session, td.training_date
from    (SELECT td1.employee_id, td1.training_date
          from training_details td1
          GROUP BY  td1.employee_id , td1.training_date
          having  count(td1.training_date) > 1) as temp
JOIN training_details as td on td.employee_id=temp.employee_id
JOIN employees as e on e.employee_id = temp.employee_id
