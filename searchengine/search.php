<html>
<head>

	<title>search engine-Search  </title>
</head>
<body>

		<h2>Search Engine</h2>
		<form action='./search.php' method='GET'>
					<input type='text' name='k' size='50' value='<?php echo $_GET['k'] ?>' />
					<input type='submit' value='search' />
		</form>
		<hr />
		<?php
				$k = $_GET['k'];
				$terms = explode(" ", $k);
				$query = "SELECT * FROM naya where ";



				foreach ($terms as $each) {
					$i = 0;

					if ( $i == 0) 

						$query .= "keywords LIKE '%$each%'";
						else
						 	
						$query .= "OR keywords LIKE '%$each%'";
						 
						
					
				}

				//connection
				mysql_connect("localhost","root","");
				mysql_select_db("engine");
				

				$query =  mysql_query("$query") or die(mysql_error());
				$numrows = mysql_num_rows($query);
				if ($numrows > 0) {
					
					while ($row = mysql_fetch_assoc($query)) {
						$id = $row['id'];
						$title = $row['title'];
						$description = $row['description'];
						$keywords = $row['keywords'];
						$link = $row['link'];

						echo "<h2><a href='$link'>$title</a></h2>
						$description<br /><br />";
					}

				}
				else
					echo "NO RESULT FOUND FOR \"<b>$k</b>\"";

				//disconnect
				mysql_close();

		?>		
			
			
</body>
</html>