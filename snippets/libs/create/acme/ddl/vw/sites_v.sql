create view sites_v as 
select ste.id  as id,
       ste.name as name,
       ste.url as url,
       ste.hashcode as hashcode,
       ste.description as description,
       ste.delay as delay,
       ste.delay_unit as delay_unit,
       ste.delay_in_seconds as delay_in_seconds,
       ste.paylimit as paylimit,
       ste.paylimit_currency as paylimit_currency,
       ste.earnings_per_visit as earnings_per_visit,
       ste.owner as owner,
       ste.created_at as created_at,
       ste.created_by as created_by,
       ste.updated_at as updated_at,
       ste.updated_by as updated_by,
       ste.paywallet as paywallet,
       ste.spe_id as spe_id,
       ste.microwallet_parameters as microwallet_parameters,
       ste.microwallet as microwallet,
       spe.sitetype as sitetype
from sites ste left join sitetypes spe on ste.spe_id = spe.id;
