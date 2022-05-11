drop procedure if exists get_user_wishlist_books ;
delimiter $$ 
create procedure get_user_wishlist_books(current_user_id int)
begin 
select 
    b.book_id ,
	b.book_name,
    b.details,
    b.author
from wishlist as w 
join book as b on w.book_id = b.book_id
where w.user_id = current_user_id;
end 
$$ 
delimiter ;

