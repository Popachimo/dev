FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)
ythtyhyt
SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'

END_COM


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)

SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'

END_COM


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)

SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'
FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)

SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'

END_COM


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)

SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'

END_COM
BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)

FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)

SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'

END_COM


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)

FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)

SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'

END_COM


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)

FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)

SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'

END_COM


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)

FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)

SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'

END_COM


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)

SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'

END_COM


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)

END_COM


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FUNCTION OPTIONS(*DIRECT)
BEGIN_COM ROLE(READ) VALIDATE(YES)

SELECT FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
FROM_FILE(#CUSTOMER)
WITH_KEY(#CUSTOMER)
WHERE_CONDITION((#CUSTOMER *EQ '123456'))

IF_STATUS IS(*OKAY)
   #MESSAGE := 'Customer found!'
ELSE
   #MESSAGE := 'Customer not found!'

END_COM


BEGIN_COM ROLE(*WEBEVENT)
DEFINE FIELD(#CUSTOMER) TYPE(*CHAR) LENGTH(10) CAPTION('Customer ID')
DEFINE FIELD(#NAME) TYPE(*CHAR) LENGTH(50) CAPTION('Name')
DEFINE FIELD(#ADDRESS) TYPE(*CHAR) LENGTH(100) CAPTION('Address')
DEFINE FIELD(#PHONE) TYPE(*CHAR) LENGTH(15) CAPTION('Phone')
DEFINE FIELD(#EMAIL) TYPE(*CHAR) LENGTH(50) CAPTION('Email')

WEB_MAP FOR(*OUTPUT) FIELDS(#CUSTOMER #NAME #ADDRESS #PHONE #EMAIL)
