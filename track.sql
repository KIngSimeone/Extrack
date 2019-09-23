create table exdate (
    id integer primary key autoincrement,
    todate date not null
    Amount integer not null,
    Expense text not null 
);
);

create table exmount (
    id integer primary key autoincrement,
    Amount integer not null,
    Expense text not null 
);
