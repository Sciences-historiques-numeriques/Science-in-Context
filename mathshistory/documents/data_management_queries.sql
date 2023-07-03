

-- Create persons from mathshistory texts' list
insert into mathshistory."instance" ("label", fk_class, definition, import_metadata)
select "name", 1, summary, concat('mathshistory_text_id: ',m.pk_mathshistory) as import
from mathshistory.mathshistory m 
order by pk_mathshistory ;

-- associate persons to mathshistory texts
insert into mathshistory.is_about ( fk_mathshistory, type_about, fk_instance, import_metadata)
select replace(import_metadata, 'mathshistory_text_id: ', '')::int pk_mathshistory, 'main_topic'::varchar, pk_instance, '20230627_1'
from mathshistory."instance" i 
where fk_class = 1;

