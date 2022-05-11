drop procedure if exists get_store_locations;
delimiter $$ 
create procedure get_store_locations()
begin 
select 
	store_id, 
	locale
from store ;
end 
$$ 
delimiter ;

