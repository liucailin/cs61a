.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = 'blue' AND pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING count(*) = 1;


CREATE TABLE matchmaker AS
  select a.pet, a.song, a.color, b.color from students as a, students as b where a.pet = b.pet and a.song = b.song and a.time < b.time;

 
CREATE TABLE sevens AS
  select seven from students, numbers where students.number = 7 and students.time = numbers.time and numbers.'7' = "True";


CREATE TABLE average_prices AS
  select category, sum(MSRP) / count(*) as average_price  from products group by category;

CREATE TABLE lowest_prices AS
  select store, item, min(price) from inventory group by item; 

CREATE TABLE lowest_cost AS
  select name from products group by category having min(products.MSRP / products.rating);


CREATE TABLE shopping_list AS
  SELECT item, store from lowest_cost, lowest_prices where item = name;


CREATE TABLE bandwidth AS
  select count(*) * Mbs as band from shopping_list, stores  where shopping_list.store = stores.store group by shopping_list.store;

CREATE TABLE total_bandwidth AS
  select sum(band) from bandwidth;

