set_ = {
    'APP_NAME' :'swiftdeploy',
    'APP_HEADER' : 'swiftdeploy',
    'APP_FOOTER':'swiftdeploy',
}

class Settings:
    pass

config = Settings()
for key, item in set_.items():
    setattr(config, key, item)
css = """:root {
    --primary: #421145;
    --tertiary: rgb(245,245,255);
    --secondary: #9c42a1;
    --text: #5f4e63;
}

body {
    background: var(--tertiary);
    color: var(--text);
}
 


header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    color: var(--tertiary);
    padding: 10px;
    box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.75);
    z-index: 9999;
    font-size: 2em;
    text-transform: capitalize;
    align-items: center;
    justify-content: center;
    display: flex;
}

.app-info{
    background: var(--tertiary);
    color: var(--text);
    padding: 20px;
    border-radius: 10px;
    margin-top:45px;
    font-size: 1.5em;
    align-items: center;
    justify-content: center;
    display: flex;
}

form{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 20px;
    font-size: 1.3em;
    text-transform: capitalize;
}

form input {
    width: 300px;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid var(--primary);
    border-radius: 5px;
}

form button {
    width: 150px;
    padding: 10px;
    background-color: var(--primary);
    color: var(--tertiary);
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background-color: var(--secondary);
}
.form-group {
    display: flex;
    justify-content: flex-start;
    align-items: center;
}

.form-group label {
    width: 100px; /* Adjust as needed */
}

.form-group input {
    flex-grow: 1;
}

footer{
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    color: var(--tertiary);
    padding: 10px;
    box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.75);
    z-index: 9999;
    font-size: 2em;
    text-transform: capitalize;
    align-items: center;
    justify-content: center;
    display: flex;   
}

"""

config.CSS = css