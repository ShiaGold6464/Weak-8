drop procedure if exists  add_user_wishlist_book;
delimiter $$ 
create procedure add_user_wishlist_book(current_user_id int, new_book_id int )
begin 
insert into  wishlist (user_id, book_id)
values (current_user_id, new_book_id);
end 
$$ 
delimiter ;