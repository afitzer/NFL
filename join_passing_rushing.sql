SELECT offensive_passing.Team, offensive_passing.`Pass Yds`, offensive_rushing.`Rush Yds`
FROM offensive_rushing
JOIN offensive_passing
ON offensive_rushing.Team=offensive_passing.Team
WHERE offensive_passing.Date is '09-28-22' AND offensive_rushing.Date is '09-28-22'
ORDER BY offensive_passing.`Pass Yds` DESC;