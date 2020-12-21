
DROP TABLE IF EXISTS details;




CREATE TABLE details (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  email TEXT NOT NULL,
  posted TEXT NOT NULL,
  time_now TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  
  
);
