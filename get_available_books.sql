drop procedure if exists get_available_books;
delimiter $$ 
create procedure get_available_books()
begin 
select 
	book_id, 
	book_name,
	author, 
	details 
from book ;
end 
$$ 
delimiter ;

