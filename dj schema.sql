
CREATE TABLE  "D_CDS"
   ("CD_NUMBER" NUMBER(5,0),
    "TITLE" VARCHAR2(50) CONSTRAINT "D_CDS_TITLE_NN" NOT NULL ENABLE,
    "PRODUCER" VARCHAR2(50) CONSTRAINT "D_CDS_PRODUCER_NN" NOT NULL ENABLE,
    "YEAR" VARCHAR2(4) CONSTRAINT "D_CDS_YEAR_NN" NOT NULL ENABLE,
     CONSTRAINT "D_CDS_CD_NUMBER_PK" PRIMARY KEY ("CD_NUMBER")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_CLIENTS"
   ("CLIENT_NUMBER" NUMBER(5,0),
    "FIRST_NAME" VARCHAR2(25) CONSTRAINT "D_CLT_FIST_NAME_NN" NOT NULL ENABLE,
    "LAST_NAME" VARCHAR2(30) CONSTRAINT "D_CLT_LAST_NAME_NN" NOT NULL ENABLE,
    "PHONE" NUMBER(15,0) CONSTRAINT "D_CLT_PHONE_NN" NOT NULL ENABLE,
    "EMAIL" VARCHAR2(50),
     CONSTRAINT "D_CLT_CLIENT_NUMBER_PK" PRIMARY KEY ("CLIENT_NUMBER")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_PACKAGES"
   ("CODE" NUMBER(10,0),
    "LOW_RANGE" NUMBER(6,0) CONSTRAINT "D_PKE_LOW_RANGE_NN" NOT NULL ENABLE,
    "HIGH_RANGE" NUMBER(6,0) CONSTRAINT "D_PKE_HIGH_RANGE_NN" NOT NULL ENABLE,
     CONSTRAINT "D_PKE_CODE_PK" PRIMARY KEY ("CODE")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_THEMES"
   ("CODE" NUMBER(10,0),
    "DESCRIPTION" VARCHAR2(100) CONSTRAINT "D_TME_DESC_NN" NOT NULL ENABLE,
     CONSTRAINT "D_TME_CODE_PK" PRIMARY KEY ("CODE")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_VENUES"
   ("ID" NUMBER(5,0),
    "LOC_TYPE" VARCHAR2(30) CONSTRAINT "D_VNE_LOC_TYPE_NN" NOT NULL ENABLE,
    "ADDRESS" VARCHAR2(100) CONSTRAINT "D_VNE_ADDRESS_NN" NOT NULL ENABLE,
    "RENTAL_FEE" VARCHAR2(50) CONSTRAINT "D_VNE_RENTAL_FEE_NN" NOT NULL ENABLE,
    "COMMENTS" VARCHAR2(100),
     CONSTRAINT "D_VNE_ID_PK" PRIMARY KEY ("ID")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_EVENTS"
   ("ID" NUMBER(5,0),
    "NAME" VARCHAR2(50) CONSTRAINT "D_EVE_NAME_NN" NOT NULL ENABLE,
    "EVENT_DATE" DATE CONSTRAINT "D_EVE_EVENT_DATE_NN" NOT NULL ENABLE,
    "DESCRIPTION" VARCHAR2(50),
    "COST" NUMBER(8,2) CONSTRAINT "D_EVE_COST_NN" NOT NULL ENABLE,
    "VENUE_ID" NUMBER(5,0) CONSTRAINT "D_EVE_VENUE_ID_NN" NOT NULL ENABLE,
    "PACKAGE_CODE" NUMBER(5,0) CONSTRAINT "D_EVE_PACKAGE_CODE_NN" NOT NULL ENABLE,
    "THEME_CODE" NUMBER(10,0) CONSTRAINT "D_EVE_THEME_CODE_NN" NOT NULL ENABLE,
    "CLIENT_NUMBER" NUMBER(5,0) CONSTRAINT "D_EVE_CLIENT_NUMBER_NN" NOT NULL ENABLE,
     CONSTRAINT "D_EVE_ID_PK" PRIMARY KEY ("ID")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_PARTNERS"
   ("ID" NUMBER(5,0),
    "FIRST_NAME" VARCHAR2(25) CONSTRAINT "D_PTR_FIRST_NAME_NN" NOT NULL ENABLE,
    "LAST_NAME" VARCHAR2(30) CONSTRAINT "D_PTR_LAST_NAME_NN" NOT NULL ENABLE,
    "EXPERTISE" VARCHAR2(25),
    "SPECIALTY" VARCHAR2(25),
    "AUTH_EXPENSE_AMT" NUMBER(8,2),
    "MANAGER_ID" NUMBER(5,0),
    "PARTNER_TYPE" VARCHAR2(25) CONSTRAINT "D_PTR_PARTNER_TYPE_NN" NOT NULL ENABLE,
     CONSTRAINT "D_PTR_ID_PK" PRIMARY KEY ("ID")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_JOB_ASSIGNMENTS"
   ("PARTNER_ID" NUMBER(5,0),
    "EVENT_ID" NUMBER(5,0),
    "JOB_DATE" DATE CONSTRAINT "D_JAT_JOB_DATE_NN" NOT NULL ENABLE,
    "STATUS" VARCHAR2(50),
     CONSTRAINT "D_JAT_PK" PRIMARY KEY ("PARTNER_ID", "EVENT_ID")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_TYPES"
   ("CODE" NUMBER(10,0),
    "DESCRIPTION" VARCHAR2(50) CONSTRAINT "D_TPE_DESC_NN" NOT NULL ENABLE,
     CONSTRAINT "D_TPE_CODE_PK" PRIMARY KEY ("CODE")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_SONGS"
   ("ID" NUMBER(5,0),
    "TITLE" VARCHAR2(50) CONSTRAINT "D_SNG_TITLE_NN" NOT NULL ENABLE,
    "DURATION" VARCHAR2(20),
    "ARTIST" VARCHAR2(20),
    "TYPE_CODE" NUMBER(5,0) CONSTRAINT "D_SNG_TYPE_CODE_NN" NOT NULL ENABLE,
     CONSTRAINT "D_SNG_ID_PK" PRIMARY KEY ("ID")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_PLAY_LIST_ITEMS"
   ("EVENT_ID" NUMBER(5,0),
    "SONG_ID" NUMBER(5,0),
    "COMMENTS" VARCHAR2(80),
     CONSTRAINT "D_PLM_PK" PRIMARY KEY ("EVENT_ID", "SONG_ID")
  USING INDEX  ENABLE
   );

CREATE TABLE  "D_TRACK_LISTINGS"
   ("SONG_ID" NUMBER(5,0),
    "CD_NUMBER" NUMBER(5,0),
    "TRACK" NUMBER(2,0) CONSTRAINT "D_TLG_TRACK_NUMBER_NN" NOT NULL ENABLE,
     CONSTRAINT "D_TLG_PK" PRIMARY KEY ("SONG_ID", "CD_NUMBER")
  USING INDEX  ENABLE
   );

ALTER TABLE  "D_EVENTS" ADD CONSTRAINT "D_EVE_CLIENT_NUMBER_FK" FOREIGN KEY ("CLIENT_NUMBER")
      REFERENCES  "D_CLIENTS" ("CLIENT_NUMBER") ENABLE;
ALTER TABLE  "D_EVENTS" ADD CONSTRAINT "D_EVE_PACKAGE_CODE_FK" FOREIGN KEY ("PACKAGE_CODE")
      REFERENCES  "D_PACKAGES" ("CODE") ENABLE;
ALTER TABLE  "D_EVENTS" ADD CONSTRAINT "D_EVE_THEME_CODE_FK" FOREIGN KEY ("THEME_CODE")
      REFERENCES  "D_THEMES" ("CODE") ENABLE;
ALTER TABLE  "D_EVENTS" ADD CONSTRAINT "D_EVE_VENUE_ID_FK" FOREIGN KEY ("VENUE_ID")
      REFERENCES  "D_VENUES" ("ID") ENABLE;
ALTER TABLE  "D_JOB_ASSIGNMENTS" ADD CONSTRAINT "D_JAT_EVENT_ID_FK" FOREIGN KEY ("EVENT_ID")
      REFERENCES  "D_EVENTS" ("ID") ENABLE;
ALTER TABLE  "D_JOB_ASSIGNMENTS" ADD CONSTRAINT "D_JAT_PARTNER_ID_FK" FOREIGN KEY ("PARTNER_ID")
      REFERENCES  "D_PARTNERS" ("ID") ENABLE;
ALTER TABLE  "D_PLAY_LIST_ITEMS" ADD CONSTRAINT "D_PLM_EVENT_ID_FK" FOREIGN KEY ("EVENT_ID")
      REFERENCES  "D_EVENTS" ("ID") ENABLE;
ALTER TABLE  "D_PLAY_LIST_ITEMS" ADD CONSTRAINT "D_PLM_SONG_ID_FK" FOREIGN KEY ("SONG_ID")
      REFERENCES  "D_SONGS" ("ID") ENABLE;
ALTER TABLE  "D_SONGS" ADD CONSTRAINT "D_SNG_TYPE_CODE_FK" FOREIGN KEY ("TYPE_CODE")
      REFERENCES  "D_TYPES" ("CODE") ENABLE;
ALTER TABLE  "D_TRACK_LISTINGS" ADD CONSTRAINT "D_TLG_CD_NUMBER_FK" FOREIGN KEY ("CD_NUMBER")
      REFERENCES  "D_CDS" ("CD_NUMBER") ENABLE;
ALTER TABLE  "D_TRACK_LISTINGS" ADD CONSTRAINT "D_TLG_SONG_ID_FK" FOREIGN KEY ("SONG_ID")
      REFERENCES  "D_SONGS" ("ID") ENABLE;

CREATE INDEX  "D_CDS_IDX" ON  "D_CDS" ("TITLE");
CREATE INDEX  "SONG_ID_IDX" ON  "D_TRACK_LISTINGS" ("SONG_ID");

-- populate tabes
INSERT INTO d_cds(cd_number,title,producer,year)
VALUES(90,'The Celebrants Live in Concert','Old Town Records','1997');
INSERT INTO d_cds(cd_number,title,producer,year)
VALUES(91,'Party Music for All Occasions','The Music Man','2000');
INSERT INTO d_cds(cd_number,title,producer,year)
VALUES(92,'Back to the Shire','Middle Earth Records','2002');
INSERT INTO d_cds(cd_number,title,producer,year)
VALUES(93,'Songs from My Childhood','Old Town Records','1999');
INSERT INTO d_cds(cd_number,title,producer,year)
VALUES(94,'Carpe Diem','R & B Inc.','2000');
INSERT INTO d_cds(cd_number,title,producer,year)
VALUES(95,'Here Comes the Bride','The Music Man','2001');
INSERT INTO d_cds(cd_number,title,producer,year)
VALUES(96,'Graduation Songbook','Tunes Are Us','1998');
INSERT INTO d_cds(cd_number,title,producer,year)
VALUES(98,'Whirled Peas','Old Town Records','2004');

INSERT INTO d_clients(client_number,first_name,last_name,phone,email)
VALUES(5922,'Hiram','Peters',3715832249,'hpeters@yahoo.com');
INSERT INTO d_clients(client_number,first_name,last_name,phone,email)
VALUES(5857,'Serena','Jones',7035335900,'serena.jones@jones.com');
INSERT INTO d_clients(client_number,first_name,last_name,phone,email)
VALUES(6133,'Lauren','Vigil',4072220090,'lbv@lbv.net');

INSERT INTO d_packages(code,low_range,high_range)
VALUES(79,500,2500);
INSERT INTO d_packages(code,low_range,high_range)
VALUES(87,2501,5000);
INSERT INTO d_packages(code,low_range,high_range)
VALUES(112,5001,10000);
INSERT INTO d_packages(code,low_range,high_range)
VALUES(200,10001,15000);

INSERT INTO d_themes(code,description)
VALUES(200,'Tropical');
INSERT INTO d_themes(code,description)
VALUES(220,'Carnival');
INSERT INTO d_themes(code,description)
VALUES(240,'Sixties');
INSERT INTO d_themes(code,description)
VALUES(110,'Classic');
INSERT INTO d_themes(code,description)
VALUES(198,'Mardi Gras');
INSERT INTO d_themes(code,description)
VALUES(454,'Eighties');
INSERT INTO d_themes(code,description)
VALUES(340,'Football');
INSERT INTO d_themes(code,description)
VALUES(502,'Fairy Tale');

INSERT INTO d_venues(id,loc_type,address,rental_fee,comments)
VALUES(100,'Private Home','52 West End Drive, Los Angeles, CA 90210','0','Large kitchen, spacious lawn');
INSERT INTO d_venues(id,loc_type,address,rental_fee,comments)
VALUES(105,'Private Home','123 Magnolia Road, Hudson, N.Y. 11220','0','3 level townhouse, speakers on all floors');
INSERT INTO d_venues(id,loc_type,address,rental_fee,comments)
VALUES(101,'Private Home','4 Primrose Lane, Chevy Chase, MD 22127','0','Gazebo, multi-level deck');
INSERT INTO d_venues(id,loc_type,address,rental_fee,comments)
VALUES(95,'School Hall','4 Mahogany Drive, Boston, MA 10010','75/hour','School closes at 10pm');
INSERT INTO d_venues(id,loc_type,address,rental_fee,comments)
VALUES(99,'National Park','87 Park Avenue, San Diego, CA 28978','400/flat fee','Bring generators');
INSERT INTO d_venues(id,loc_type,address,rental_fee,comments)
VALUES(220,'Hotel','200 Pennsylvania Ave, Washington D.C. 09002','300/per person','Classy affair, tight security, private entrance for vendors');

INSERT INTO d_events(client_number,id,name,event_date,description,cost,venue_id,package_code,theme_code)
VALUES(5922,100,'Peters Graduation',TO_DATE('05-14-2004','mm-dd-yyyy'),'Party for 200, red, white, blue motif',8000,100,112,200);
INSERT INTO d_events(client_number,id,name,event_date,description,cost,venue_id,package_code,theme_code)
VALUES(6133,105,'Vigil wedding',TO_DATE('04-28-2004','mm-dd-yyyy'),'Black tie at Four Season hotel',10000,220,200,200);

INSERT INTO d_partners(id,first_name,last_name,expertise,specialty,auth_expense_amt,manager_id,partner_type)
VALUES(11,'Jennifer','cho','Weddings','All Types',NULL,33,'Wedding Coordinator');
INSERT INTO d_partners(id,first_name,last_name,expertise,specialty,auth_expense_amt,manager_id,partner_type)
VALUES(22,'Jason','Tsang',NULL,'Hip Hop',NULL,33,'Disk Jockey');
INSERT INTO d_partners(id,first_name,last_name,expertise,specialty,auth_expense_amt,manager_id,partner_type)
VALUES(33,'Allison','Plumb','Event Planning',NULL,300000,33,'Manager');

INSERT INTO d_job_assignments(partner_id,event_id,job_date,status)
VALUES(11,105,TO_DATE('02-02-2004','mm-dd-yyyy'),'Visited');

INSERT INTO d_types(code,description)
VALUES(1,'Jazz');
INSERT INTO d_types(code,description)
VALUES(12,'Pop');
INSERT INTO d_types(code,description)
VALUES(40,'Reggae');
INSERT INTO d_types(code,description)
VALUES(88,'Country');
INSERT INTO d_types(code,description)
VALUES(77,'New Age');

INSERT INTO d_songs(id,title,duration,artist,type_code)
VALUES(45,'Its Finally Over','5 min','The Hobbits',12);
INSERT INTO d_songs(id,title,duration,artist,type_code)
VALUES(46,'Im Going to Miss My Teacher','2 min','Jane Pop',12);
INSERT INTO d_songs(id,title,duration,artist,type_code)
VALUES(47,'Hurrah for Today','3 min','The Jubilant Trio',77);
INSERT INTO d_songs(id,title,duration,artist,type_code)
VALUES(48,'Meet Me At the Altar','6 min','Bobby West',1);
INSERT INTO d_songs(id,title,duration,artist,type_code)
VALUES(49,'Lets Celebrate','8 min','The Celebrants',77);
INSERT INTO d_songs(id,title,duration,artist,type_code)
VALUES(50,'All These Years','10 min','Diana Crooner',88);

INSERT INTO d_play_list_items(event_id,song_id,comments)
VALUES(100,45,'Play late');
INSERT INTO d_play_list_items(event_id,song_id,comments)
VALUES(100,46,NULL);
INSERT INTO d_play_list_items(event_id,song_id,comments)
VALUES(100,47,'Play early');
INSERT INTO d_play_list_items(event_id,song_id,comments)
VALUES(105,48,'Play after cake cutting');
INSERT INTO d_play_list_items(event_id,song_id,comments)
VALUES(105,49,'Play first');
INSERT INTO d_play_list_items(event_id,song_id,comments)
VALUES(105,47,'Play for the father');

INSERT INTO d_track_listings(song_id,cd_number,track)
VALUES(45,92,1);
INSERT INTO d_track_listings(song_id,cd_number,track)
VALUES(46,93,1);
INSERT INTO d_track_listings(song_id,cd_number,track)
VALUES(47,91,2);
INSERT INTO d_track_listings(song_id,cd_number,track)
VALUES(48,95,5);
INSERT INTO d_track_listings(song_id,cd_number,track)
VALUES(49,91,3);
