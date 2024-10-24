-- Lists all cities in hbtn_0d_usa

SELECT cities.id, city.name, state.name FROM cites LEFT JOIN states ON cities.states_id = states.id;
