import CastManager from '../../components/CastManager/CastManager';
import { Container } from '@mui/material';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

function AudioPlayer() {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Container maxWidth="md">
        <header className="player-header">
          <h3>
            Pi Stream Cast
          </h3>
        </header>
        <CastManager />
      </Container>
    </ThemeProvider>
  );
}

export default AudioPlayer;