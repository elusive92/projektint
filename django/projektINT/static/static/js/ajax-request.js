$(document).ready(function() {
   
    function isUrl(str) {
      var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
      '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.?)+[a-z]{2,}|'+ // domain name
      '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
      '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
      '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
      '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
      return pattern.test(str);
    }
   
   var getRequest = function() {
   
        setTimeout(function() {
    
            $.ajax({
                
                url: 'http://192.168.0.105:8000/api/v1/mediarequest/',
                data: {
                    'username': 'admin',
                    'api_key': '65714eec974d6ac96f6f3d6dce2f8050fe250ecf',
                    'format': 'json'
                },
                dataType: 'json',
                
                complete: function() {
                    getRequest();  
                },
                
                success: function(data) {
                    var object = data.objects;
                    var tabContent = $('#payload tbody');
                    console.log(tabContent);
                    
                    for(var i in object) {
                        var isPhoto = isUrl(object[i].payload);
                        var payload = isPhoto ? '<img src="' : '';
                        payload += object[i].payload;
                        payload += isPhoto ? '">' : '';
                        
                        var html = '<tr><td>'+payload+'</td><td></td></tr>';
                        $(tabContent).append(html);
                    }
                    
                },
                
                error: function(xhr, error, status) {
                    
                }
                
            });
            
        }, 2000);  
    
   }
   
   getRequest();
   
});