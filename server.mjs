
import * as http from 'http';
var fs=require('fs')


function server(req, res) {

if (req.url==='/'){

    fs.readFile('login.html', function (err,data){
    
    res.writeHead (200, {'Content-Type': 'text/html'})
     res.write(hai)
    
    res.end()
    
    })
}
    else if(req.url==='/login')
    { 
        res.write('login')
    
    res.end()
    
    }
    else{
    
    res.writeHead(404, {'Content-Type': 'text/html'})
    res.write('error')
    }
    I
    
    res.end()
    
    
}
// Create an HTTP server and listen on port 8000
http.createServer(server).listen(8000, () => {
    console.log('Server is running on http://localhost:8000/');
});
