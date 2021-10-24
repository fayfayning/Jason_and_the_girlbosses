import React, { Component } from "react";
import {
  Button,
  Form,
  FormGroup,
  Input,
  Label,
  Container,
  Row,
  Col
} from "reactstrap";
import happy from "./Moodlets/Happy_Cat.jpg";
import sad from "./Moodlets/Sad_Cat.jpg";
import angry from "./Moodlets/Angry_Cat.jpg";
import anxious from "./Moodlets/Anxious_Cat.jpg";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };



  render() {
    const { onSave } = this.props;

    return (
      <Form>
        <FormGroup>
            <Label for='mood-pictures'></Label>
                <Container>
                    <Row>
                        <Col>
                            <img src={happy} onClick={this.imageClick}/>
                        </Col>
                        <Col>
                            <img src={sad} onClick={this.imageClick}/>
                        </Col>
                        <Col>
                            <img src={angry} onClick={this.imageClick}/>
                        </Col>
                        <Col>
                            <img src={anxious} onClick={this.imageClick}/>
                        </Col>
                    </Row>
                </Container>
            </FormGroup>
            <FormGroup>
              <Label for="todo-title">Title</Label>
              <Input
                type="text"
                id="mood-status"
                name="mood-status"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="Enter Todo Title"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-description">Do you want to add any notes?</Label>
              <Input
                type="text"
                id="todo-description"
                name="description"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter Todo description"
              />
            </FormGroup>
          </Form>
    );
  }
}