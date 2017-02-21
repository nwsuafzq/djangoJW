<script>
	    function validateForm()
	    {
		    var status = document.getElementById("error");
  		    var pattern = /^\d{10}$/;
  		    if (!pattern.test(myForm.username.value))
  		    {
  			    status.innerHTML = "学号为10位数字";
  			    return false;
  		    }
  		    return true;
        }
        </script>