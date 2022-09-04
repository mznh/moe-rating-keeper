create table players(
  id integer primary key autoincrement,
  key  text , -- これもprimaryを期待、認証に用いる
  token text, -- これはnameとの組合せでprimaryを期待 
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
  info  text,
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
  style   integer,
  rating  numeric, 
  sigma   numeric, 
  created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
  updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
);

-- seed
insert 
  into styles(name, info) 
  values
    ("ガチ","ガチです。"),
    ("カジュアル","カジュアルです。"),
    ("ノーレート","レイティングを計算したくないけど、戦績を記録したい場合はこちらを使用してください");

insert 
  into formats(name,info)
  values
    ("無課金オンリー","無課金技,装備だけでやります。"),
    ("フォーマットサンプル","アレとソレとコレだけでやります"),
    ("カジュアル","制限はありません、対戦相手との合意の上ですべてが許されます。");
