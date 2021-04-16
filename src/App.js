import React, { useState, useEffect } from "react";
import { AppBar, Toolbar, Grid, Typography, makeStyles } from "@material-ui/core";
import MediaCard from "./components/MediaCard";

const useStyles = makeStyles((theme) => ({
  grid: {
    flexGrow: 1,
    margin: theme.spacing(4),
  },
}));

function App() {
  const classes = useStyles();

  const kittens = [
    { imgUrl: "http://placekitten.com/200/300", title: "Kitten", body: "Cute kitten" },
    { imgUrl: "http://placekitten.com/300/300", title: "Kitto", body: "Cute kitto" },
    { imgUrl: "http://placekitten.com/200/100", title: "Kato", body: "Cute kato" },
    { imgUrl: "http://placekitten.com/100/100", title: "Katia", body: "Cute katia" },
  ];

  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("/message")
      .then((res) => res.json())
      .then((data) => {
        setMessage(data.message);
      });
  }, []);

  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Posts
          </Typography>
        </Toolbar>
      </AppBar>

      <Grid container spacing={4} className={classes.grid}>
        {kittens.map((content) => (
          <Grid item xs={6} md={3}>
            <MediaCard content={content} />
          </Grid>
        ))}
      </Grid>
      <p>The current message is {message}</p>
    </div>
  );
}

export default App;
