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
        # this.load.setBaseURL = 'http://labs.phaser.io/'  

        this.load.image('sky', 'assets/space3.png')
        this.load.image('logo', 'assets/logo.svg')
        this.load.image('red', 'assets/red.png')

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

def display_keyCode(ev):
    print("keyCode = ", ev.keyCode)
    # if ev.keyCode == 81:  # q or Q
    #     doc.unbind("keydown")
    # ev.preventDefault()

doc.bind("keydown", display_keyCode)
