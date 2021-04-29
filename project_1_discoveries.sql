#possible driver for churn rate and my discoveries

#automatic forms of payment help increase profits while decreasing churn rate

select count(*)
from customers
where contract_type_id = 1;

#3875 month to month customers

select count(*)
from customers
where contract_type_id = 1 and (payment_type_id = 3 or payment_type_id = 4);

#of those 3875 month to month users 1132 customers use automatic forms of payment (29%)

select count(*)
from customers
where contract_type_id = 1 and (payment_type_id = 3 or payment_type_id = 4) and  churn = 'No';

#of the 1132 customers with automatic payments 753 have not churned (66%)

select sum(tenure)
from customers
where contract_type_id = 1 and (payment_type_id = 3 or payment_type_id = 4);

#sum of total for month to month customers without automatic payments : 3213557

select sum(total_charges)
from customers
where contract_type_id = 1 and (payment_type_id = 1 or payment_type_id = 2);

#sum of total for month to month customers with automatic payments : 2092304 total:5305861 

select sum(total_charges)
from customers
where contract_type_id = 1 and (payment_type_id = 3 or payment_type_id = 4);

#40% total profits come from users with outomatic payments (29%)














