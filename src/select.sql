SELECT *
FROM siren_93_coord
WHERE ST_DistanceSphere(the_geom, ST_GeomFromText('POINT(2.5078809957 48.8619914902)', 4326)) < 50
--AND libapet = ''