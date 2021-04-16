import { Card, CardActions, CardMedia, CardActionArea, CardContent } from "@material-ui/core";
import { Typography, Button, makeStyles } from "@material-ui/core";

const useStyles = makeStyles({
  root: {
    maxWidth: 345,
  },
});

export default function MediaCard(props) {
  const classes = useStyles();
  return (
    <Card className={classes.root}>
      <CardActionArea>
        <CardMedia
          component="img"
          className={classes.media}
          image={props.content.imgUrl}
          height="200"
          title="Kitten"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {props.content.title}
          </Typography>
          <Typography gutterBottom variant="body2" component="h6">
            {props.content.date || "Abr 16"}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            {props.content.body}
          </Typography>
        </CardContent>
      </CardActionArea>

      <CardActions>
        <Button size="small" color="primary">
          Read more
        </Button>
      </CardActions>
    </Card>
  );
}
