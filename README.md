# Bluesquare full-stack development assignment

This repo contains the instruction for the completion of the **Full stack developer** assignment.

This assignment takes the form of a **small realistic project**, to be developed as a little **single-page app**.

It will be used to assess the candidate skill levels, and also their ability to work with modern development tool and 
practices, such as Git/Github, Docker, etc...

**We expect you to dedicate between 3-4 hours of work to this exercise**. It's ok if not everything is perfect or 100% 
finished, the idea is not to spend a lot of time on this but rather what you can come up with in a few hours.

## The project: a release checklist

The goal of this small assignment is to build a very small but fully functioning modern web application.

This application is a release checklist tool that could help developers with their release process.

![alt text](https://github.com/BLSQ/full-stack-assignment/blob/main/releasecheck.png?raw=true)

You can findThe above mock-ups in the `wireframes` directory of this repository.

The application has only one main model: the `Release`. A `Release` is composed of multiple `Step`s and has the 
following properties :

- A name (`text`, mandatory)
- A date (`datetime`, mandatory)
- A status (`planned|ongoing|done`, auto)
- Additional info (`text`, optional)

A release keeps track of the state of the different steps (either `true` or `false`).

The `status` is not chosen by the end user, it is simply computed from the steps state :

- No step completed : `planned`
- At least one step completed : `ongoing`
- All steps completed : `done`

For the sake of this example, let's assume that a release is done in 7 steps

1. Check that all relevant GitHub pull requests have been merged
2. Make sure that the CHANGELOG.md files in each relevant repository have been updated for the release
3. All tests are passing
4. Creating releases in the different GitHub repositories used by the project
5. Deploy the release to the demo or staging environment
6. Manually test each feature / bug fix that is part of the release
7. Deploy the release to production

## Running the code

*This section should be updated with the required instructions to run your project*.

## Assignment tasks

### Must-have

In terms of features :

- [ ] Users should be able to view a list of all the releases
- [ ] Users should be able to create a new release (with a name, due date, and optional "additional information")
- [ ] Users should be able to check / uncheck the steps that are part of a release
- [ ] Users should be able to update the release additional information

In terms of technical constraints :

- [ ] The whole codebase should be contained in a single repository
- [ ] The end result should be a single-page application
- [ ] `React` should be used for the frontend, and `Python` for the backend (ideally Django)
- [ ] The application state should be stored in a `PostgreSQL` or `MySQL` database
- [ ] The frontend and the backend should communicate using an API
- [ ] No advanced graphic design is needed, but there should be a decent UX with a few well-thought CSS rules
- [ ] There should be a small `README.md` file with the instructions needed to run the code locally

**Please note that this shouldn't be a multi-user application**. It does not need any kind of user management.

### Nice-to-have :

In terms of features :

- [ ] Users could be able to delete a release
- [ ] Users could benefit from a responsive 

Regarding the tech :

- [ ] The frontend and backend could use `GraphQL` as the API layer
- [ ] The backend can be easily run with `Docker` (`Dockerfile` + `docker-compose.yaml`)
- [ ] The codebase contain a couple of automated tests


## Where to start :

1. Fork this repository
2. Write the project code (3-4 hours)
3. Update this `README.md` file with installation instructions (see "Running the code" above)
4. That's it - we'll review your work together once you are done
