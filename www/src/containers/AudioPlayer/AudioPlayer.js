import './AudioPlayer.css';
import MediaControls from '../../components/MediaControls/MediaControls';
import CastManager from '../../components/CastManager/CastManager';

function AudioPlayer() {
  return (
    <div className="audio-player">
      <header className="player-header">
        <h3>
          Pi Stream Cast
        </h3>
      </header>
      <CastManager />
      <MediaControls />
    </div>
  );
}

export default AudioPlayer;