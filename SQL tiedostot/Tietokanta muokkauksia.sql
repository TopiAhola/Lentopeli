
-- Muokkaus 1:
-- Lisätään kentat tauluun sarake country_fi jossa on maan nimi suomeksi.
-- Siltä varalta, että tarvitaan myöhemmin.
alter table kentat
add column country_fi varchar(40) NULL;


--Muokkaus 2:
--lisätää kentat tauluun GDP ja syötetään arvot:

alter table kentat
add column GDP int;

UPDATE kentat SET GDP = '6' WHERE iso_country = 'AL';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'AD';
UPDATE kentat SET GDP = '54' WHERE iso_country = 'AT';
UPDATE kentat SET GDP = '10' WHERE iso_country = 'BY';
UPDATE kentat SET GDP = '50' WHERE iso_country = 'BE';
UPDATE kentat SET GDP = '7' WHERE iso_country = 'BA';
UPDATE kentat SET GDP = '11' WHERE iso_country = 'BG';
UPDATE kentat SET GDP = '16' WHERE iso_country = 'HR';
UPDATE kentat SET GDP = '26' WHERE iso_country = 'CZ';
UPDATE kentat SET GDP = '67' WHERE iso_country = 'DK';
UPDATE kentat SET GDP = '26' WHERE iso_country = 'EE';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'FO';
UPDATE kentat SET GDP = '56' WHERE iso_country = 'FI';
UPDATE kentat SET GDP = '45' WHERE iso_country = 'FR';
UPDATE kentat SET GDP = '54' WHERE iso_country = 'DE';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'GI';
UPDATE kentat SET GDP = '20' WHERE iso_country = 'GR';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'GG';
UPDATE kentat SET GDP = '18' WHERE iso_country = 'HU';
UPDATE kentat SET GDP = '72' WHERE iso_country = 'IS';
UPDATE kentat SET GDP = '95' WHERE iso_country = 'IE';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'IM';
UPDATE kentat SET GDP = '35' WHERE iso_country = 'IT';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'JE';
UPDATE kentat SET GDP = '4' WHERE iso_country = 'XK';
UPDATE kentat SET GDP = '20' WHERE iso_country = 'LV';
UPDATE kentat SET GDP = '184' WHERE iso_country = 'LI';
UPDATE kentat SET GDP = '22' WHERE iso_country = 'LT';
UPDATE kentat SET GDP = '139' WHERE iso_country = 'LU';
UPDATE kentat SET GDP = '32' WHERE iso_country = 'MT';
UPDATE kentat SET GDP = '3' WHERE iso_country = 'MD';
UPDATE kentat SET GDP = '234' WHERE iso_country = 'MC';
UPDATE kentat SET GDP = '10' WHERE iso_country = 'ME';
UPDATE kentat SET GDP = '62' WHERE iso_country = 'NL';
UPDATE kentat SET GDP = '7' WHERE iso_country = 'MK';
UPDATE kentat SET GDP = '82' WHERE iso_country = 'NO';
UPDATE kentat SET GDP = '15' WHERE iso_country = 'PL';
UPDATE kentat SET GDP = '25' WHERE iso_country = 'PT';
UPDATE kentat SET GDP = '15' WHERE iso_country = 'RO';
UPDATE kentat SET GDP = '12' WHERE iso_country = 'RU';
UPDATE kentat SET GDP = '52' WHERE iso_country = 'SM';
UPDATE kentat SET GDP = '9' WHERE iso_country = 'RS';
UPDATE kentat SET GDP = '22' WHERE iso_country = 'SK';
UPDATE kentat SET GDP = '28' WHERE iso_country = 'SI';
UPDATE kentat SET GDP = '31' WHERE iso_country = 'ES';
UPDATE kentat SET GDP = '60' WHERE iso_country = 'SE';
UPDATE kentat SET GDP = '95' WHERE iso_country = 'CH';
UPDATE kentat SET GDP = '4' WHERE iso_country = 'UA';
UPDATE kentat SET GDP = '46' WHERE iso_country = 'GB';
UPDATE kentat SET GDP = '21' WHERE iso_country = 'VA';


--- Muokkaus 3
-- kirjoitusasun muokkauksia

update kentat set country_fi = "Venäjä" where iso_country = "RU";
update kentat set country_fi = "Valko-Venäjä" where iso_country = "BY";
update kentat set country_fi = "Itävalta" where iso_country = "AT";
update kentat set country_fi = "Tsekki" where iso_country = "CZ";
update kentat set country_fi = "Färsaaret" where iso_country = "FO";


