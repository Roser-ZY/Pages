---
title: "Force-Directed Graph 实现方案"
author: "Roser"
date: 2025-01-10
image: "images/content/Algorithm.png"
draft: false
tags:
  - Algorithm
  - Force-Directed
  - GraphLayout
---
力导向图（*Force-Directed Graph*）算法是以比较美观的方式绘制网状图的 Obsidian 的关系图谱使用。

[C++ 实现方案](https://stackoverflow.com/questions/713701/force-directed-layout-implementation-in-c) 建议使用 Boost Graph 实现，Boost 提供了一些图算法。

[JS 实现方案](https://stackoverflow.com/questions/62286695/is-there-a-simple-ish-algorithm-for-drawing-force-directed-graphs) 的源码：

```ts
var noNodes = 100;
var noConn = 50;
var gravityConstant = 1.1;
var forceConstant = 1000;
var physics = true;

var nodes = [];
var nodeCon = [];
var clicked = false;
var lerpValue = 0.2;
var startDisMultiplier = 10;
var closeNode;
var closeNodeMag;


function setup() {
  createCanvas(600, 600);
  fill(0)
  for (let i = 0; i < noNodes; i++) {
    let x = random(-startDisMultiplier*width , startDisMultiplier*width)
    let y = random(-startDisMultiplier*height , startDisMultiplier*height)
    node = new Node(createVector(x, y), random(1, 5))
    nodes.push(node);
  }
  closeNode = nodes[0]
  for (let n = 0; n < noConn; n++) {
    nodeCon.push([
      round(random(noNodes - 1)),
      round(random(noNodes - 1)),
      random(100, 300)
    ])
  }
  nodeCon.push([0,1,200])
  
  // lets add a connection from all solo nodes for good measure
  
  let connected = new Set()
  nodeCon.forEach(conn=>{
    connected.add(conn[0])
    connected.add(conn[1])
  })
  
  for (let n = 0; n < noNodes; n++) {
    if (!connected.has(n)){
        nodeCon.push([
          n, 
          round(random(noNodes - 1)), 
          random(100, 300)
          ]
        )
    }
  }
}

function draw() {
  translate(width / 2, height / 2)
  background(255);
    nodeCon.forEach(con => {
    node1 = nodes[con[0]]
    node2 = nodes[con[1]]
    line(node1.pos.x, node1.pos.y,
      node2.pos.x, node2.pos.y)
  })
  applyForces(nodes)
  nodes.forEach(node => {
    node.draw()
    if (physics) {
      node.update()
    }
  })
  if (clicked == true) {
    let mousePos = createVector(mouseX-width/2, mouseY-height/2)
    closeNode.pos.lerp(mousePos, lerpValue)
    if (lerpValue < 0.95) {
        lerpValue+=0.02;
    }
  }
}

function touchStarted() {
    clicked = true
    let mousePos = createVector(mouseX-width/2, mouseY-height/2)
    nodes.forEach((node)=>{
      if (mousePos.copy().sub(node.pos).mag() - closeNode.mass/(2 * PI) < mousePos.copy().sub(closeNode.pos).mag() - closeNode.mass/(2 * PI))
        closeNode = node;
    })
}

function touchEnded() {
    clicked = false
    lerpValue = 0.2
}

function applyForces(nodes) {

  // apply force towards centre
  nodes.forEach(node => {
    gravity = node.pos.copy().mult(-1).mult(gravityConstant)
    node.force = gravity
  })

  // apply repulsive force between nodes
  for (let i = 0; i < nodes.length; i++) {
    for (let j = i + 1; j < nodes.length; j++) {
      pos = nodes[i].pos
      dir = nodes[j].pos.copy().sub(pos)
      force = dir.div(dir.mag() * dir.mag())
      force.mult(forceConstant)
      nodes[i].force.add(force.copy().mult(-1))
      nodes[j].force.add(force)
    }
  }

  // apply forces applied by connections
  nodeCon.forEach(con => {
    let node1 = nodes[con[0]]
    let node2 = nodes[con[1]]
    let maxDis = con[2]
    let dis = node1.pos.copy().sub(node2.pos)
    diff = dis.mag() - maxDis
    node1.force.sub(dis)
    node2.force.add(dis)
  })
}

function Node(pos, size) {
  this.pos = pos
  this.force = createVector(0, 0)
  this.mass = (2 * PI * size)/1.5
  this.fs = []
}

Node.prototype.update = function() {
  force = this.force.copy()
  vel = force.copy().div(this.mass)
  // print("VEL", vel, "FORCE", force)
  this.pos.add(vel)
}

Node.prototype.draw = function() {
  ellipse(this.pos.x, this.pos.y, this.mass, this.mass)
}
```