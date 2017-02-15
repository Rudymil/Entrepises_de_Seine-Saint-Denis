CREATE TABLE "siren_93" (
	"id" serial NOT NULL UNIQUE,
	"siren" varchar(30) NOT NULL,
	"l1_normalisee" varchar(50) NOT NULL,
	"adresse" varchar(255) NOT NULL,
	"libapet" varchar(255),
	"libtefet" varchar(255),
	"libnj" varchar(255),
	CONSTRAINT siren_93_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "bano_93" (
	"id" serial NOT NULL UNIQUE,
	"adresse" varchar(255) NOT NULL,
	CONSTRAINT bano_93_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

SELECT AddGeometryColumn('bano_93','the_geom','4326','POINT',2);