import React, { Component } from "react";
// import logo from "./logo.svg";
// import "./App.css";

// import { sideBar } from "./semantic/dist/components/sidebar";
import { Header, Icon, Image, Menu, Segment, Sidebar } from "semantic-ui-react";

// use electron stuff
// const electron = window.require("electron");
//
// const fs = electron.remote.require("fs");
// const ipcRenderer = electron.ipcRenderer;
// https://medium.freecodecamp.org/building-an-electron-application-with-create-react-app-97945861647c

class App extends Component {
  render() {
    return (
      <React.Fragment>
        <Sidebar.Pushable as={Segment}>
          <Sidebar
            as={Menu}
            animation="overlay"
            icon="labeled"
            inverted
            vertical
            visible
            width="thin"
          >
            <Menu.Item as="a">
              <Icon name="home" />
              Home
            </Menu.Item>
            <Menu.Item as="a">
              <Icon name="gamepad" />
              Games
            </Menu.Item>
            <Menu.Item as="a">
              <Icon name="camera" />
              Channels
            </Menu.Item>
          </Sidebar>

          <Sidebar.Pusher>
            <Segment basic>
              <Header as="h3">Application Content</Header>
              <Image src="/images/wireframe/paragraph.png" />
            </Segment>
          </Sidebar.Pusher>
        </Sidebar.Pushable>
      </React.Fragment>
    );
  }
}

export default App;
