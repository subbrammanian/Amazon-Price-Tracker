#Table creation
create table if not exists AMAZON_PRICE_TRACKER.USERS(
USERID INTEGER AUTOINCREMENT PRIMARY KEY,
EMAIL TEXT NOT NULL,
PASSWORD TEXT NOT NULL
);

create table if not exists AMAZON_PRICE_TRACKER.SUBSCRIPTIONS(
	SUBID INTEGER AUTOINCREMENT PRIMARY KEY,
	PRODUCTURL TEXT NOT NULL,
	USER INTEGER,
	FOREIGN KEY(USER) REFERENCES USERS(USERID)
);


COMMIT;

#Index creation

create unique index EMAIL_INDEX ON USERS (EMAIL);
COMMIT;



#Select queries
#To list the current subscriptions
select PRODUCTURL from SUBSCRIPTIONS s inner join USERS u on s.USER=u.USERID where u.EMAIL=<current_username>

#To delete a specific subscription
delete from SUBSCRIPTIONS s inner join USERS u on s.USER=u.USERID where u.EMAIL= <>  and  s.PRODUCTURL = <>

#To delete all subscriptions
delete from SUBSCRIPTIONS s inner join USERS u on s.USER=u.USERID where u.EMAIL= <> 


