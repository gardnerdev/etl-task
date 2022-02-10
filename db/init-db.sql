DROP DATABASE IF EXISTS dwh;
CREATE DATABASE dwh;

CREATE USER dwh;

GRANT ALL PRIVILEGES ON DATABASE dwh TO dwh;
GRANT ALL ON schema public TO dwh;


\c dwh dwh;
CREATE SCHEMA dwh;

DROP TABLE IF EXISTS dwh.customer_visits;

CREATE TABLE IF NOT EXISTS customer_visits (
    id	               SERIAL NOT NULL PRIMARY KEY,
    ad_bucket          VARCHAR(8),
    ad_type            VARCHAR (8),
    ad_source          VARCHAR(8),
    schema_version     INT,
    ad_campaign_id     INT,
    ad_keyword         VARCHAR(10),
    ad_group_id        INT,
    ad_creative        INT,
    utm_campaign       INT,
    utm_content        VARCHAR(15),
    utm_medium         VARCHAR(3),
    utm_source         VARCHAR(8),
    utm_term           VARCHAR(10),
UNIQUE(id)
);
CREATE INDEX idx_id ON customer_visits (id);