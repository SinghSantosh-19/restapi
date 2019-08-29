
# local modules
import config
import dbi
import endpoints

# Get the application instance
app = config.app



if __name__=='__main__':
    dbi.initialize_db()
    app.run(debug=True)

