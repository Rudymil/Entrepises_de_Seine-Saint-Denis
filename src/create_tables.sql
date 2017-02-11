CREATE TABLE "Siren_93" (
	"id" serial NOT NULL,
	"siren" varchar(30) NOT NULL UNIQUE,
	"l1_normalisee" varchar(50) NOT NULL UNIQUE,
	"l4_normalisee" varchar(255) NOT NULL,
	"codpos" varchar(5) NOT NULL,
	"libcom" varchar(25) NOT NULL,
	"libapet" varchar(255),
	"libtefet" varchar(255),
	"libnj" varchar(255),
	CONSTRAINT Siren_93_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "Bano_93" (
	"id" serial NOT NULL,
	"voirie" varchar(255) NOT NULL UNIQUE,
	"codpos" varchar(255) NOT NULL,
	"libcom" varchar(25) NOT NULL,
	"lat" varchar(15) NOT NULL,
	"lon" varchar(15) NOT NULL,
	CONSTRAINT Bano_93_pk PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);