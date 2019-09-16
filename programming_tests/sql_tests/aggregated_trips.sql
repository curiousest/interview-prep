# https://leetcode.com/problems/trips-and-users/

select Request_at as Day, ROUND(COUNT(IF(Status != "completed", True, Null))/COUNT(*), 2) as 'Cancellation Rate'
from Trips t 
where Client_id not in (select Users_Id from Users where Banned="Yes")
and Driver_Id not in (select Users_Id from Users where Banned="Yes")
and Request_at >= '2013-10-01' and Request_at <= '2013-10-03'
GROUP BY Request_at