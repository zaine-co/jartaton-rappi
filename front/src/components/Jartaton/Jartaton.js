import React from 'react';
import { Card, Button, CardTitle, CardText } from 'reactstrap';
import SearchBar from '../Ui/SearchBar/SearchBar';

const Jartaton = (props) => {
    return (
        <div>
            <Card body outline color="danger">
                <CardTitle>
                    <SearchBar/>
                </CardTitle>
                <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
            </Card>
        </div>
  );
};

export default Jartaton;