CREATE TABLE "siren_93" (
	"id" serial NOT NULL UNIQUE,
	"siren" varchar(30) NOT NULL UNIQUE,
	"l1_normalisee" varchar(50) NOT NULL,
	"adresse" varchar(255) NOT NULL UNIQUE,
	"libapet" varchar(255),
	"libtefet" varchar(255),
	"libnj" varchar(255),
	CONSTRAINT siren_93_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "bano_93" (
	"id" serial NOT NULL UNIQUE,
	"adresse" varchar(255) NOT NULL UNIQUE,
	"lat" FLOAT(15) NOT NULL,
	"lon" FLOAT(15) NOT NULL,
	CONSTRAINT bano_93_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);