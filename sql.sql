SELECT user_id, COUNT(DISTINCT created_at) as count FROM 
  (SELECT user_messages.user_id, user_messages.created_at, date.last_date FROM
    (SELECT user_id, created_at::timestamp::date FROM messages 
      WHERE agent_id is NULL) as user_messages, 
        (SELECT MAX(created_at::timestamp::date) as last_date FROM messages) as date
          WHERE DATE_PART('day',last_date::timestamp - created_at::timestamp) < 7) as last_week 
            GROUP BY user_id 
                HAVING COUNT(DISTINCT created_at) >= 4
