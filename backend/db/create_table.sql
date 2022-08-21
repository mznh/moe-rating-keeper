create table players(
  id integer primary key autoincrement,
  key  text,
  name  text,
  server  text,
  info  text,
  created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
  updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
);

create table battles(
  id integer primary key autoincrement,
  name  text,
  server  text,
  info  text
  side_a integer,
  side_b integer,
  winner integer,
  style integer, -- etc) 1 styleId
  format text, -- etc) 1,2,3,4 formatIds
  created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
  updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
);

-- styles は ガチ カジュアル ノーレート だけの前提
create table styles(
  id integer primary key autoincrement,
  name  text,
  info  text,
  created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
  updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
);

create table formats(
  id integer primary key autoincrement,
  name  text,
  info  text,
  created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
  updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
);

create table rating_logs (
  id integer primary key autoincrement,
  player_id  integer,
  style  text,
  rating  numeric, 
  created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
  updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
);
