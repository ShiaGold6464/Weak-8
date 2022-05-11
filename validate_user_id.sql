drop procedure if exists  validate_user_id;
delimiter $$ 
create procedure validate_user_id(current_user_id int)
begin 
select count(*) as user_count
from user 
where user_id =  current_user_id;
end 
$$ 
delimiter ;