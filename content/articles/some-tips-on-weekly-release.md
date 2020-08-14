---
Title: Some tips I learned managing weekly release for 50M+ users’ app
Date: 2020-08-22
Tags: computing, daily-life, communication
Slug: some-tips-on-weekly-release
Status: Draft
Summary: Some tips I learned managing weekly release for 50M+ users’ app
---

# Some tips I learned managing weekly release for 50M+ users’ app

In any game, war, or enterprise resource management, the last thing you want is to underestimate your opponent(s). In release management, your opponent is “chaos”. As a release manager, the last thing you should expect is that everything will go as planned.


### Is the “release frequency” on point ?

Please, first and foremost, note that a weekly (even bi-weekly) release-cycle isn’t suitable for every other app, be it a mobile app or an enterprise-grade SaaS. Before jumping the bandwagon, please consider the frequency of features you might push out every cycle and how many people will be able to focus on this weekly (or bi-weekly) release-cycle. Having a shiny process, just for the sake of having it, is an easy recipe for disaster. Especially, if your QA/testing team isn’t well-distributed as per the app areas, to provide final sign-off on that specific scope, avoid intense weekly releases.


### Is the process well-documented & communicated?

Well accepted process document is the key, works as the manifesto. In the case of confusion or conflict between the teams, there are two options



*   It’s already in the doc, point to it
*   If it’s not in the doc or not clear enough, an opportunity to improve

Lookout for scalability. You can ping (aka “pull”) 3 persons for info, not 30. So, establish some “push notification” method. E.g., comment on the G.sheet, or Jira comment.


### Is some automation missing ? 

Identify the opportunities to automate. As an RM, if you need something to do more than twice a day, start there. Have you been asked the same question twice? Include the answer in a FAQ doc.

Document the need, identify the tool required. It can be as simple as a SQL query, a Python script, or a much more complex system. 

Before driving into the thing, identify the matrix to monitor the improvement, and get approval (at least, verbally) from the stakeholders.

Some example automation tool I use:

*   [Google script](https://www.google.com/script/start/) to monitor changes on Google Sheet
*   [Slack bot response](https://slack.com/help/articles/202026038-An-introduction-to-Slackbot) for selected keywords
*   Python scripts for compiling custom JIRA reports. [An example](https://gist.github.com/kmonsoor/62ed1bc6cd3084648245073744182227)
*   [Email forwarding to Slack DM](https://slack.com/intl/en-sg/help/articles/206819278-Send-emails-to-Slack)


### Is “Divide & Conquer” properly deployed ?

This DC method/mechanism/scheme (as a fan of Marvel, I don’t mind the name mixup though :P ) is a well hated term outside the programmer community while widely practiced inside because of the different contexts. But it’s also well known in different industries as “division of labor.” Regardless of the name and the flavor, it’s essential for the successful execution of weekly release cycles. 

*   Design the process and its breakdown based on the roles, not the actual persons or their skillset
*   Minimize switching between roles for individual persons in a single release cycle. e.g., if someone, in the QA team, is writing test cases, let them do that for at least for the time period. If someone is testing individual features at the beginning of the week, let her continue it until the end of the release week.
*   Keep only integrated test (staging, then production) dependency for release rollout. For individual features, the developing team(s) should take care of it, before declaring it ready for shipping. The “not ready to be shipped” features must be isolated from the production scope, excluding from the ongoing release cycle.
*   Imagine the shipment process of a newer version as a concept like a train and different teams as different product pipelines. Products come to the train station only when it’s packed and ready to be shipped. I believe tt’s an agile concept
*   Like a public train, the release “train” should depart as per schedule. If any feature is delayed due to unforeseen reason or a recently discovered severe bug, the release-train should not wait for it. Rather, once the feature is stabilized later, it should wait for the next train.
*   Adopting the concept of a train and its scheduled departure and well-documented checkpoints (i.e. phases) enables a large organization to expect and likewise communicate what to expect when.


### Are you deploying on a bad moon-phase?

Probably, it should be a piece of common knowledge. Be it a backend deployment or app rollout on app stores, please avoid changing anything with the “production” tag, before a weekend or a multi-day holiday. 

Like the [printer meme](https://twitter.com/System32Comics/status/1266100094853476352/photo/1), the universe throws us unthinkable issues after weekend deployments.


### Provision for backup

Plan capacity with some slack. I’d suggest going for the 80/20 rule, meaning the weekly release should be able to go out, even in the unavailability of 20% human resources. 

Unlike machines, people will be sick, go out for vacation, emergency travel plans, unexpectedly resign etc. anything can happen. So, like any other robust system design, plan for “disaster”. 


### Continuous Integration/Deployment

To have an effective release process, automated and well-documented CI/CD pipeline is almost a prerequisite.



*   Developers across the board, by themselves, should be able to build, test, merge their code, and build the binary from the latest stable and/or release checkpoints.
*   Once their change, be it a feature or a bugfix, is ready to be merged with the release branch, a complete suite of automated tests should be run on the resultant binary to detect any regression bug due to the change; with no dependency on the release team
*   QA, while testing for a particular release, should be able to receive regression or production build without any manual intervention from the release team


### Continuous feedback & evolution

An efficient release-train process is an intensive process. And, no process can be perfect from the beginning. Every organization has, like its own fingerprint, has different priorities, deliverables, audience, resources, and of course budget. So, while it can start with an agile blueprint, it needs to be well fit on its organizational body. Hence, comes the requirement for continuous feedback from the participants, stakeholders, and even the release team-members.


### Stay on the “good book” of the app stores

If the app is in the center of revenue of your company, keep a close eye on the regular comm from the app stores, i.e. Google Play and Apple Appstore. It’s very easy to miss these communications among other regular stuff.

Regardless of how ridiculous your company feels about some policies on the app stores, please read between the lines. In case of confusion, read again. Especially, if you’re one of the big fishes.

I think it’s quite common that they weren’t strictly monitoring or enforcing compliance of some policies last month, but don’t even think they aren’t going to enforce tomorrow and reject your app. The release manager or the team, being the interface with the app stores, should frequently communicate with the stakeholders and the product team so that they carefully go through relevant app store policies long before they invest company time and resources into a feature or a roadmap. Trust me, it happens more than anyone likes to admit, that after month-long design and development the app update with the feature gets rejected on the app stores, solely due to this new feature.

If possible, try to get hold of and build a working relationship with the business development or dev support teams of Google and Apple. It might help in case of any misunderstanding and/or some negotiations about the compliance timeline.


### Notes:
*   Please don’t take the number 50M+ literally. The actual number is much higher, but should be considered as company secrets ;). Right?
*   This is NOT a definitive process guide and I’m not an expert on Agile methodologies. I’m just trying to share my learning from my release experience of 1.75 years. Some stuff might help any other release manager on the planet.
