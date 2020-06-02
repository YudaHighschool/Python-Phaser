from browser import window, document
import javascript

Phaser = window.Phaser

class Game(object):
    def __init__(self):
        self.game = window.Phaser.Game.new(
            {
                'type': Phaser.AUTO,
                'width': 800,
                'height': 600,
                'physics': {
                    'default': 'arcade',
                    'arcade': {
                        'gravity': {'y': 200}
                    }
                },
                'scene': {
                    'preload': self.preload,
                    'create': self.create
                }
            }
        )

    def preload(self, *args):
        this = javascript.this()
        this.load.setBaseURL = 'http://labs.phaser.io'  

        this.load.image('sky', 'https://images.unsplash.com/photo-1474573892045-721452c3d98c?ixlib=rb-0.3.5&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjE0NTg5fQ&s=8a1c8e04786fad38cae94ee48ce372e7')
        this.load.image('logo', 'https://yd-main.web.app/assets/favicon/android-chrome-192x192.png')
        this.load.image('red', 'assets/particles/red.png')

    def create(self, *args):
        this = javascript.this()
        this.add.image(400, 300, 'sky')

        particles = this.add.particles('red')
        emitter = particles.createEmitter({
            'speed': 100,
            'scale': {'start': 1, 'end': 0},
            'blendMode': 'NORMAL'
        })

        logo = this.physics.add.image(400, 100, 'logo')

        logo.setVelocity(200, 100)
        logo.setBounce(1, 1)
        logo.setCollideWorldBounds(True)

        emitter.startFollow(logo)


GAME = Game()
