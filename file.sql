CREATE DATABASE task_app;

create table bugs
(bugId int primary key auto_increment,
deviceId int,
testerId int,
foreign key(deviceId) references devices(deviceId),
foreign key(testerId) references testers(testerId)
);

create table devices
(deviceId int primary key auto_increment,
description varchar(60)
);

create table testers
(testerId int primary key auto_increment,
firstName varchar(60),
lastName varchar(60),
coutry varchar(5),
lastLogin datetime
);

create table tester_device
(testerId int not null,
deviceId int not null,
foreign key(testerId) references testers(testerId),
foreign key(deviceId) references devices(deviceId)
);