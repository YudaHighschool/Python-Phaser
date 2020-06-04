from browser import window, document, html
import javascript

# 設定 Python 執行結果的容器　
container = document['python']  # 　Python 執行結果　<div id="python"></div>
for c in "w3-margin-top w3-margin".split(' '):  # 設定基本版型
    container.classList.add(c)
container.style = {"width": "800px"}
container <= html.DIV(html.H2('Phaser 遊戲設計'),  Class="w3-container w3-blue")

phaserContainer = html.DIV(id="phaser")
container <= phaserContainer

Phaser = window.Phaser


class Game(object):
    def __init__(self):
        self.game = Phaser.Game.new(
            {
                'type': Phaser.AUTO,
                'width': 800,
                'height': 400,
                'parent': 'phaser',
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


document.bind("keydown", display_keyCode)
