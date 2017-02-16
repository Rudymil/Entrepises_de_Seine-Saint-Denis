CREATE TABLE siren_93_coord AS
SELECT siren_93.id, siren_93.siren, siren_93.l1_normalisee, siren_93.adresse, bano_93.the_geom, siren_93.libapet, siren_93.libtefet, siren_93.libnj 
FROM siren_93
INNER JOIN bano_93
ON siren_93.adresse = bano_93.adresse